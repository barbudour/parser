# ClientRegistrator.RegisterExtensions - метод
Выполняет регистрацию расширений. Рекомендуется не выполнять регистрацию Unity
в этом объекте.
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public override void RegisterExtensions(
    	IExtensionContainer extensionContainer
    )
VB __Копировать
     Public Overrides Sub RegisterExtensions ( 
    	extensionContainer As IExtensionContainer
    )
C++ __Копировать
     public:
    virtual void RegisterExtensions(
    	IExtensionContainer^ extensionContainer
    ) override
F# __Копировать
     abstract RegisterExtensions : 
            extensionContainer : IExtensionContainer -> unit 
    override RegisterExtensions : 
            extensionContainer : IExtensionContainer -> unit 
#### Параметры
extensionContainer
[IExtensionContainer](T_Tessa_Extensions_IExtensionContainer.htm)
    Контейнер расширений, в котором выполняется регистрация.
#### Реализации
[IRegistrator.RegisterExtensions(IExtensionContainer)](M_Tessa_Extensions_IRegistrator_RegisterExtensions.htm)  
##  __См. также
#### Ссылки
[ClientRegistrator -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_ClientRegistrator.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)
