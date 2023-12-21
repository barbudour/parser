# RegistratorBase.InitializeExtensions - метод
Выполняет инициализацию заданного контейнера расширений. Рекомендуется не
выполнять регистрацию Unity в этом объекте.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public virtual void InitializeExtensions(
    	IExtensionContainer extensionContainer
    )
VB __Копировать
     Public Overridable Sub InitializeExtensions ( 
    	extensionContainer As IExtensionContainer
    )
C++ __Копировать
     public:
    virtual void InitializeExtensions(
    	IExtensionContainer^ extensionContainer
    )
F# __Копировать
     abstract InitializeExtensions : 
            extensionContainer : IExtensionContainer -> unit 
    override InitializeExtensions : 
            extensionContainer : IExtensionContainer -> unit 
#### Параметры
extensionContainer
[IExtensionContainer](T_Tessa_Extensions_IExtensionContainer.htm)
    Контейнер расширений, для которого выполняется инициализация.
#### Реализации
[IRegistrator.InitializeExtensions(IExtensionContainer)](M_Tessa_Extensions_IRegistrator_InitializeExtensions.htm)  
##  __См. также
#### Ссылки
[RegistratorBase - ](T_Tessa_Extensions_RegistratorBase.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
