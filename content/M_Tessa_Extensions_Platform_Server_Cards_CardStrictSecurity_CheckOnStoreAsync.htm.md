# CardStrictSecurity.CheckOnStoreAsync - метод
Проверяет доступ к карточке при её сохранении с ограничением flag.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.Cards](N_Tessa_Extensions_Platform_Server_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected virtual ValueTask<bool> CheckOnStoreAsync(
    	ICardStoreExtensionContext storeContext,
    	ConfigurationFlags flag
    )
VB __Копировать
     Protected Overridable Function CheckOnStoreAsync ( 
    	storeContext As ICardStoreExtensionContext,
    	flag As ConfigurationFlags
    ) As ValueTask(Of Boolean)
C++ __Копировать
     protected:
    virtual ValueTask<bool> CheckOnStoreAsync(
    	ICardStoreExtensionContext^ storeContext, 
    	ConfigurationFlags flag
    )
F# __Копировать
     abstract CheckOnStoreAsync : 
            storeContext : ICardStoreExtensionContext * 
            flag : ConfigurationFlags -> ValueTask<bool> 
    override CheckOnStoreAsync : 
            storeContext : ICardStoreExtensionContext * 
            flag : ConfigurationFlags -> ValueTask<bool> 
#### Параметры
storeContext
[ICardStoreExtensionContext](T_Tessa_Cards_Extensions_ICardStoreExtensionContext.htm)
    Контекст расширения на сохранение карточки.
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
