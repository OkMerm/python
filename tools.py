# -*- coding: utf-8 -*-
import math
import numpy 
from sources import Source1D


class GaussianMod(Source1D):
    '''
    Источник, создающий дифференцированный гауссов импульс
    '''

    def __init__(self, magnitude, dg, wg):
        '''
        magnitude - максимальное значение в источнике;
        dg - коэффициент, задающий начальную задержку гауссова импульса;
        wg - коэффициент, задающий ширину гауссова импульса.
        '''
        self.magnitude = magnitude
        self.dg = dg
        self.wg = wg
        self.Nl= 40
        self.Sc = 1
        self.eps = 9
        self.mu = 1

    def getFieldE(self, m, q):
        '''
        Расчет поля E в дискретной точке пространства m
        в дискретный момент времени q
        '''
        return (numpy.sin(2 * numpy.pi / self.Nl * (q * self.Sc - m * numpy.sqrt(self.eps * self.mu))) *
                numpy.exp(-(((q - m * numpy.sqrt(self.eps * self.mu) / self.Sc) - self.dg) / self.wg) ** 2))
    
class LayerContinuous:
    def __init__(self,
                 xmin: float,
                 xmax: float = None,
                 eps: float = 1.0,
                 mu: float = 1.0,
                 sigma: float = 0.0):
        self.xmin = xmin
        self.xmax = xmax
        self.eps = eps
        self.mu = mu
        self.sigma = sigma

class LayerDiscrete:
    def __init__(self,
                 xmin: int,
                 xmax: int = None,
                 eps: float = 1.0,
                 mu: float = 1.0,
                 sigma: float = 0.0):
        self.xmin = xmin
        self.xmax = xmax
        self.eps = eps
        self.mu = mu
        self.sigma = sigma

class Sampler:
    def __init__(self, discrete: float):
        self.discrete = discrete

    def sample(self, x: float) -> int:
        return math.floor(x / self.discrete + 0.5)

def sampleLayer(layer_cont: LayerContinuous, sampler: Sampler) -> LayerDiscrete:
    start_discrete = sampler.sample(layer_cont.xmin)
    end_discrete = (sampler.sample(layer_cont.xmax)
                    if layer_cont.xmax is not None
                    else None)
    return LayerDiscrete(start_discrete, end_discrete,
                         layer_cont.eps, layer_cont.mu, layer_cont.sigma)
