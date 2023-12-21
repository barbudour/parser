# CardWithoutLockingStrategy - конструктор
Создаёт экземпляр класса с указанием его зависимостей.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardWithoutLockingStrategy(
    	IDbScope dbScope,
    	IConfigurationInfoProvider configurationInfoProvider
    )
VB __Копировать
     Public Sub New ( 
    	dbScope As IDbScope,
    	configurationInfoProvider As IConfigurationInfoProvider
    )
C++ __Копировать
     public:
    CardWithoutLockingStrategy(
    	IDbScope^ dbScope, 
    	IConfigurationInfoProvider^ configurationInfoProvider
    )
F# __Копировать
     new : 
            dbScope : IDbScope * 
            configurationInfoProvider : IConfigurationInfoProvider -> CardWithoutLockingStrategy
#### Параметры
dbScope [IDbScope](T_Tessa_Platform_Data_IDbScope.htm)
    Объект, обеспечивающий взаимодействие с базой данных.
configurationInfoProvider
[IConfigurationInfoProvider](T_Tessa_Platform_Runtime_IConfigurationInfoProvider.htm)
    Провайдер информации о конфигурации.
##  __См. также
#### Ссылки
[CardWithoutLockingStrategy - ](T_Tessa_Cards_CardWithoutLockingStrategy.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
