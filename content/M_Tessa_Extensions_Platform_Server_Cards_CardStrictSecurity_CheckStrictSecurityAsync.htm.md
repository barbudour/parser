# CardStrictSecurity.CheckStrictSecurityAsync - метод
Проверяет доступ к карточке при наличии ограничения
[StrictSecurity](T_Tessa_Platform_Runtime_ConfigurationFlags.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.Cards](N_Tessa_Extensions_Platform_Server_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public virtual ValueTask<bool> CheckStrictSecurityAsync(
    	ICardExtensionContext context
    )
VB __Копировать
     Public Overridable Function CheckStrictSecurityAsync ( 
    	context As ICardExtensionContext
    ) As ValueTask(Of Boolean)
C++ __Копировать
     public:
    virtual ValueTask<bool> CheckStrictSecurityAsync(
    	ICardExtensionContext^ context
    )
F# __Копировать
     abstract CheckStrictSecurityAsync : 
            context : ICardExtensionContext -> ValueTask<bool> 
    override CheckStrictSecurityAsync : 
            context : ICardExtensionContext -> ValueTask<bool> 
#### Параметры
context
[ICardExtensionContext](T_Tessa_Cards_Extensions_ICardExtensionContext.htm)
    Контекст расширения карточки.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
Возвращает true, если доступ к карточке есть, иначе false
#### Реализации
[ICardStrictSecurity.CheckStrictSecurityAsync(ICardExtensionContext)](M_Tessa_Extensions_Platform_Server_Cards_ICardStrictSecurity_CheckStrictSecurityAsync.htm)  
##  __См. также
#### Ссылки
[CardStrictSecurity -
](T_Tessa_Extensions_Platform_Server_Cards_CardStrictSecurity.htm)
[Tessa.Extensions.Platform.Server.Cards - пространство
имён](N_Tessa_Extensions_Platform_Server_Cards.htm)
