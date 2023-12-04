# -*- coding: utf-8 -*-
import os
import pdb
import psutil
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .utils import listar_discos, listar_contenido_carpeta

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        listdisk = listar_discos()
        context.update({'listdisk': listdisk})
        # pdb.set_trace()
        return context


class DiskLocal(LoginRequiredMixin, TemplateView):
    template_name = 'home/disklocal.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DiskLocal, self).get_context_data(*args, **kwargs)
        disk = self.kwargs.get('disk')
        path = "{}:/".format(disk)
        disks = listar_contenido_carpeta(path)
        context.update({'disks': disks})
        return context


class DiskFolderLocal(LoginRequiredMixin, TemplateView):
    template_name = 'home/folderlocal.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DiskFolderLocal, self).get_context_data(*args, **kwargs)
        disk = self.kwargs.get('disk')
        folder = self.kwargs.get('folder')
        path = "{}:/{}".format(disk,folder)
        folders = listar_contenido_carpeta(path)
        context.update({'folders': folders})
        return context


class DiskFolderLocal2(LoginRequiredMixin, TemplateView):
    template_name = 'home/folderlocal2.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DiskFolderLocal2, self).get_context_data(*args, **kwargs)
        disk = self.kwargs.get('disk')
        folder = self.kwargs.get('folder')
        folder2 = self.kwargs.get('folder2')
        path = "{}:/{}/{}".format(disk, folder, folder2)
        folders = listar_contenido_carpeta(path)
        context.update({'folders': folders})
        return context


class RDSView(LoginRequiredMixin, TemplateView):
    template_name = 'home/rds.html'

    def get_context_data(self, *args, **kwargs):
        context = super(RDSView, self).get_context_data(*args, **kwargs)
        return context


class WorkspaceView(LoginRequiredMixin, TemplateView):
    template_name = 'home/workspace.html'

    def get_context_data(self, *args, **kwargs):
        context = super(WorkspaceView, self).get_context_data(*args, **kwargs)
        return context
