# CardStrictSecurity.CheckOnDeleteAsync - метод
Проверяет доступ к карточке при её удалении с ограничением flag.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.Cards](N_Tessa_Extensions_Platform_Server_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected virtual ValueTask<bool> CheckOnDeleteAsync(
    	ICardDeleteExtensionContext deleteContext,
    	ConfigurationFlags flag
    )
VB __Копировать
     Protected Overridable Function CheckOnDeleteAsync ( 
    	deleteContext As ICardDeleteExtensionContext,
    	flag As ConfigurationFlags
    ) As ValueTask(Of Boolean)
C++ __Копировать
     protected:
    virtual ValueTask<bool> CheckOnDeleteAsync(
    	ICardDeleteExtensionContext^ deleteContext, 
    	ConfigurationFlags flag
    )
F# __Копировать
     abstract CheckOnDeleteAsync : 
            deleteContext : ICardDeleteExtensionContext * 
            flag : ConfigurationFlags -> ValueTask<bool> 
    override CheckOnDeleteAsync : 
            deleteContext : ICardDeleteExtensionContext * 
            flag : ConfigurationFlags -> ValueTask<bool> 
#### Параметры
deleteContext
[ICardDeleteExtensionContext](T_Tessa_Cards_Extensions_ICardDeleteExtensionContext.htm)
    Контекст расширения на удаление карточки.
flag [ConfigurationFlags](T_Tessa_Platform_Runtime_ConfigurationFlags.htm)
    Флаг, определяющий уровень ограничений системы.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
Возвращает true, если доступ к карточке есть, иначе false.
##  __См. также
#### Ссылки
[CardStrictSecurity -
](T_Tessa_Extensions_Platform_Server_Cards_CardStrictSecurity.htm)
[Tessa.Extensions.Platform.Server.Cards - пространство
имён](N_Tessa_Extensions_Platform_Server_Cards.htm)
