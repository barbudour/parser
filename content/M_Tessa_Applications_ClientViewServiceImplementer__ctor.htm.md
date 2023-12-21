# ClientViewServiceImplementer - конструктор
Initializes a new instance of the
[ClientViewServiceImplementer](T_Tessa_Applications_ClientViewServiceImplementer.htm)
class. Инициализирует новый экземпляр класса
[Object](https://learn.microsoft.com/dotnet/api/system.object).
## __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ClientViewServiceImplementer(
    	[NotNullAttribute] IEnumerable<ITessaView> clientViews,
    	[NotNullAttribute] IViewCurrentUserParameters parametersProvider,
    	[NotNullAttribute] Func<ITessaViewService> serviceFactory
    )
VB __Копировать
     Public Sub New ( 
    	<NotNullAttribute> clientViews As IEnumerable(Of ITessaView),
    	<NotNullAttribute> parametersProvider As IViewCurrentUserParameters,
    	<NotNullAttribute> serviceFactory As Func(Of ITessaViewService)
    )
C++ __Копировать
     public:
    ClientViewServiceImplementer(
    	[NotNullAttribute] IEnumerable<ITessaView^>^ clientViews, 
    	[NotNullAttribute] IViewCurrentUserParameters^ parametersProvider, 
    	[NotNullAttribute] Func<ITessaViewService^>^ serviceFactory
    )
F# __Копировать
     new : 
            [<NotNullAttribute>] clientViews : IEnumerable<ITessaView> * 
            [<NotNullAttribute>] parametersProvider : IViewCurrentUserParameters * 
            [<NotNullAttribute>] serviceFactory : Func<ITessaViewService> -> ClientViewServiceImplementer
#### Параметры
clientViews
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[ITessaView](T_Tessa_Views_ITessaView.htm)>
     Список клиентский [представлений](T_Tessa_Views_ITessaView.htm). Как правило представления зарегистрированные в контейнере. 
parametersProvider
[IViewCurrentUserParameters](T_Tessa_Views_IViewCurrentUserParameters.htm)
     Провайдер специальных параметров 
serviceFactory
[Func](https://learn.microsoft.com/dotnet/api/system.func-1)<[ITessaViewService](T_Tessa_Views_ITessaViewService.htm)>
     Фабрика обращения к [сервису представлений](T_Tessa_Views_ITessaViewService.htm)
##  __См. также
#### Ссылки
[ClientViewServiceImplementer -
](T_Tessa_Applications_ClientViewServiceImplementer.htm)
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
