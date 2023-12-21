# OpenInModalDialogOnDoubleClickExtensionConfigurator.GetConfiguratorFormAsync
- метод
Возвращает форму конфигуратора расширения.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Cards](N_Tessa_Extensions_Platform_Client_Cards.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public override ValueTask<(IFormViewModel , Action )> GetConfiguratorFormAsync(
    	IExtensionConfigurationContext context,
    	Action modifiedAction,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Overrides Function GetConfiguratorFormAsync ( 
    	context As IExtensionConfigurationContext,
    	modifiedAction As Action,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of ( As IFormViewModel,  As Action))
C++ __Копировать
     public:
    virtual ValueTask<ValueTuple<IFormViewModel^, Action^>> GetConfiguratorFormAsync(
    	IExtensionConfigurationContext^ context, 
    	Action^ modifiedAction, 
    	CancellationToken cancellationToken = CancellationToken()
    ) override
F# __Копировать
     abstract GetConfiguratorFormAsync : 
            context : IExtensionConfigurationContext * 
            modifiedAction : Action * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<ValueTuple<IFormViewModel, Action>> 
    override GetConfiguratorFormAsync : 
            context : IExtensionConfigurationContext * 
            modifiedAction : Action * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<ValueTuple<IFormViewModel, Action>> 
#### Параметры
context
[IExtensionConfigurationContext](T_Tessa_UI_Views_Extensions_IExtensionConfigurationContext.htm)
     Контекст конфигурации расширения 
modifiedAction [Action](https://learn.microsoft.com/dotnet/api/system.action)
     Callback для объекта, вызывающего форму, сообщающий, что данные в форме изменены. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[ValueTuple](https://learn.microsoft.com/dotnet/api/system.valuetuple-2)<[IFormViewModel](T_Tessa_UI_Cards_IFormViewModel.htm),
[Action](https://learn.microsoft.com/dotnet/api/system.action)>>  
Форма конфигуратора расширения и Callback для сохраеннения настроек
расширения.
#### Реализации
[IExtensionSettingsConfigurator.GetConfiguratorFormAsync(IExtensionConfigurationContext,
Action,
CancellationToken)](M_Tessa_UI_Views_Extensions_IExtensionSettingsConfigurator_GetConfiguratorFormAsync.htm)  
##  __См. также
#### Ссылки
[OpenInModalDialogOnDoubleClickExtensionConfigurator -
](T_Tessa_Extensions_Platform_Client_Cards_OpenInModalDialogOnDoubleClickExtensionConfigurator.htm)
[Tessa.Extensions.Platform.Client.Cards - пространство
имён](N_Tessa_Extensions_Platform_Client_Cards.htm)
