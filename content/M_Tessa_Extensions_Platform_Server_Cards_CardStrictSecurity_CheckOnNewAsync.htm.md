# CardStrictSecurity.CheckOnNewAsync - метод
Проверяет доступ к карточке при её создании с ограничением flag.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.Cards](N_Tessa_Extensions_Platform_Server_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected virtual ValueTask<bool> CheckOnNewAsync(
    	ICardNewExtensionContext newContext,
    	ConfigurationFlags flag
    )
VB __Копировать
     Protected Overridable Function CheckOnNewAsync ( 
    	newContext As ICardNewExtensionContext,
    	flag As ConfigurationFlags
    ) As ValueTask(Of Boolean)
C++ __Копировать
     protected:
    virtual ValueTask<bool> CheckOnNewAsync(
    	ICardNewExtensionContext^ newContext, 
    	ConfigurationFlags flag
    )
F# __Копировать
     abstract CheckOnNewAsync : 
            newContext : ICardNewExtensionContext * 
            flag : ConfigurationFlags -> ValueTask<bool> 
    override CheckOnNewAsync : 
            newContext : ICardNewExtensionContext * 
            flag : ConfigurationFlags -> ValueTask<bool> 
#### Параметры
newContext
[ICardNewExtensionContext](T_Tessa_Cards_Extensions_ICardNewExtensionContext.htm)
    Контекст расширения на создание карточки.
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
