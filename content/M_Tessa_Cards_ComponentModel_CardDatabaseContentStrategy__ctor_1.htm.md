# CardDatabaseContentStrategy(IDbScope, ICardFileSource) - конструктор
Создаёт экземпляр класса с указанием его области видимости объекта
[DbManager](T_Tessa_Platform_Data_DbManager.htm).
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardDatabaseContentStrategy(
    	IDbScope dbScope,
    	ICardFileSource settings
    )
VB __Копировать
     Public Sub New ( 
    	dbScope As IDbScope,
    	settings As ICardFileSource
    )
C++ __Копировать
     public:
    CardDatabaseContentStrategy(
    	IDbScope^ dbScope, 
    	ICardFileSource^ settings
    )
F# __Копировать
     new : 
            dbScope : IDbScope * 
            settings : ICardFileSource -> CardDatabaseContentStrategy
#### Параметры
dbScope [IDbScope](T_Tessa_Platform_Data_IDbScope.htm)
    Область видимости объекта [DbManager](T_Tessa_Platform_Data_DbManager.htm).
settings [ICardFileSource](T_Tessa_Cards_ICardFileSource.htm)
    Настройки по местоположению контента файла.
##  __См. также
#### Ссылки
[CardDatabaseContentStrategy -
](T_Tessa_Cards_ComponentModel_CardDatabaseContentStrategy.htm)
[CardDatabaseContentStrategy -
перегрузка](Overload_Tessa_Cards_ComponentModel_CardDatabaseContentStrategy__ctor.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
