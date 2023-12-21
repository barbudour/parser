# TessaApplicationProcessVersionServiceHost - конструктор
Инициализирует новый экземпляр класса
[TessaApplicationProcessVersionServiceHost](T_Tessa_Applications_Services_PlatformApplication_TessaApplicationProcessVersionServiceHost.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Applications.Services.PlatformApplication](N_Tessa_Applications_Services_PlatformApplication.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public TessaApplicationProcessVersionServiceHost(
    	Func<int, ITessaApplicationServiceHost> resolveServiceHostByVersionApiFunc,
    	Func<int> getVersionApiFunc
    )
VB __Копировать
     Public Sub New ( 
    	resolveServiceHostByVersionApiFunc As Func(Of Integer, ITessaApplicationServiceHost),
    	getVersionApiFunc As Func(Of Integer)
    )
C++ __Копировать
     public:
    TessaApplicationProcessVersionServiceHost(
    	Func<int, ITessaApplicationServiceHost^>^ resolveServiceHostByVersionApiFunc, 
    	Func<int>^ getVersionApiFunc
    )
F# __Копировать
     new : 
            resolveServiceHostByVersionApiFunc : Func<int, ITessaApplicationServiceHost> * 
            getVersionApiFunc : Func<int> -> TessaApplicationProcessVersionServiceHost
#### Параметры
resolveServiceHostByVersionApiFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[Int32](https://learn.microsoft.com/dotnet/api/system.int32),
[ITessaApplicationServiceHost](T_Tessa_Applications_Services_PlatformApplication_ITessaApplicationServiceHost.htm)>
getVersionApiFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-1)<[Int32](https://learn.microsoft.com/dotnet/api/system.int32)>
## __См. также
#### Ссылки
[TessaApplicationProcessVersionServiceHost -
](T_Tessa_Applications_Services_PlatformApplication_TessaApplicationProcessVersionServiceHost.htm)
[Tessa.Applications.Services.PlatformApplication - пространство
имён](N_Tessa_Applications_Services_PlatformApplication.htm)
