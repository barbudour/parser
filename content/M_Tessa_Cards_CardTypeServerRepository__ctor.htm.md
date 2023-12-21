# CardTypeServerRepository - конструктор
Создаёт экземпляр класса с указанием области видимости объекта
[Tessa.Platform.Data.DbManager].
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardTypeServerRepository(
    	IDbScope dbScope,
    	IBulkInsertExecutor bulkInsertExecutor
    )
VB __Копировать
     Public Sub New ( 
    	dbScope As IDbScope,
    	bulkInsertExecutor As IBulkInsertExecutor
    )
C++ __Копировать
     public:
    CardTypeServerRepository(
    	IDbScope^ dbScope, 
    	IBulkInsertExecutor^ bulkInsertExecutor
    )
F# __Копировать
     new : 
            dbScope : IDbScope * 
            bulkInsertExecutor : IBulkInsertExecutor -> CardTypeServerRepository
#### Параметры
dbScope [IDbScope](T_Tessa_Platform_Data_IDbScope.htm)
     Область видимости объекта [Tessa.Platform.Data.DbManager]. 
bulkInsertExecutor
[IBulkInsertExecutor](T_Tessa_Platform_Data_IBulkInsertExecutor.htm)
## __См. также
#### Ссылки
[CardTypeServerRepository - ](T_Tessa_Cards_CardTypeServerRepository.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
