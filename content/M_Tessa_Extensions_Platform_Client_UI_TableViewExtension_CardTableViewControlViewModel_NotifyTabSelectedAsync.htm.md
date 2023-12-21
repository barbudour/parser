# CardTableViewControlViewModel.NotifyTabSelectedAsync - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.UI.TableViewExtension](N_Tessa_Extensions_Platform_Client_UI_TableViewExtension.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public override Task NotifyTabSelectedAsync(
    	ITabSelectedContext context,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Overrides Function NotifyTabSelectedAsync ( 
    	context As ITabSelectedContext,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    virtual Task^ NotifyTabSelectedAsync(
    	ITabSelectedContext^ context, 
    	CancellationToken cancellationToken = CancellationToken()
    ) override
F# __Копировать
     abstract NotifyTabSelectedAsync : 
            context : ITabSelectedContext * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override NotifyTabSelectedAsync : 
            context : ITabSelectedContext * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
context [ITabSelectedContext](T_Tessa_UI_Cards_ITabSelectedContext.htm)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)
#### Реализации
[ISupportTabNotifications.NotifyTabSelectedAsync(ITabSelectedContext,
CancellationToken)](M_Tessa_UI_Cards_ISupportTabNotifications_NotifyTabSelectedAsync.htm)  
##  __См. также
#### Ссылки
[CardTableViewControlViewModel -
](T_Tessa_Extensions_Platform_Client_UI_TableViewExtension_CardTableViewControlViewModel.htm)
[Tessa.Extensions.Platform.Client.UI.TableViewExtension - пространство
имён](N_Tessa_Extensions_Platform_Client_UI_TableViewExtension.htm)
