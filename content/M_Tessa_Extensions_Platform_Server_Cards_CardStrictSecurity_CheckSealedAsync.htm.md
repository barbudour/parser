# CardStrictSecurity.CheckSealedAsync - метод
Проверяет доступ к карточке при наличии ограничения
[Sealed](T_Tessa_Platform_Runtime_ConfigurationFlags.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.Cards](N_Tessa_Extensions_Platform_Server_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public virtual ValueTask<bool> CheckSealedAsync(
    	ICardExtensionContext context
    )
VB __Копировать
     Public Overridable Function CheckSealedAsync ( 
    	context As ICardExtensionContext
    ) As ValueTask(Of Boolean)
C++ __Копировать
     public:
    virtual ValueTask<bool> CheckSealedAsync(
    	ICardExtensionContext^ context
    )
F# __Копировать
     abstract CheckSealedAsync : 
            context : ICardExtensionContext -> ValueTask<bool> 
    override CheckSealedAsync : 
            context : ICardExtensionContext -> ValueTask<bool> 
#### Параметры
context
[ICardExtensionContext](T_Tessa_Cards_Extensions_ICardExtensionContext.htm)
    Контекст расширения карточки.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
Возвращает true, если доступ к карточке есть, иначе false
#### Реализации
[ICardStrictSecurity.CheckSealedAsync(ICardExtensionContext)](M_Tessa_Extensions_Platform_Server_Cards_ICardStrictSecurity_CheckSealedAsync.htm)  
##  __См. также
#### Ссылки
[CardStrictSecurity -
](T_Tessa_Extensions_Platform_Server_Cards_CardStrictSecurity.htm)
[Tessa.Extensions.Platform.Server.Cards - пространство
имён](N_Tessa_Extensions_Platform_Server_Cards.htm)
