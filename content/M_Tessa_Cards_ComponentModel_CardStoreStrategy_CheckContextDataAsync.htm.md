# CardStoreStrategy.CheckContextDataAsync - метод
Выполняет проверки в базе данных по информации, сохранённой в контексте.
Например, проверяет, что задания, которые берутся в работу, фактически ещё не
были взяты в работу и не были завершены. Рекомендуется выполнять внутри
блокировки на запись карточки перед любыми действиями, связанными с изменением
данных. Возвращает признак того, что все проверки выполнены успешно. Если
метод возвращает false, то рекомендуется прервать сохранение карточки.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<bool> CheckContextDataAsync(
    	CardStoreContext context,
    	DbManager db
    )
VB __Копировать
     Public Function CheckContextDataAsync ( 
    	context As CardStoreContext,
    	db As DbManager
    ) As Task(Of Boolean)
C++ __Копировать
     public:
    virtual Task<bool>^ CheckContextDataAsync(
    	CardStoreContext^ context, 
    	DbManager^ db
    ) sealed
F# __Копировать
     abstract CheckContextDataAsync : 
            context : CardStoreContext * 
            db : DbManager -> Task<bool> 
    override CheckContextDataAsync : 
            context : CardStoreContext * 
            db : DbManager -> Task<bool> 
#### Параметры
context [CardStoreContext](T_Tessa_Cards_ComponentModel_CardStoreContext.htm)
    Контекст сохранения карточки.
db [DbManager](T_Tessa_Platform_Data_DbManager.htm)
    Объект, используемый для доступа к базе данных.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
true, если все проверки выполнены успешно; false, если возникли ошибки,
которые записаны в результат валидации в объекте context. В этом случае
рекомендуется прервать сохранение карточки.
#### Реализации
[ICardStoreStrategy.CheckContextDataAsync(CardStoreContext,
DbManager)](M_Tessa_Cards_ComponentModel_ICardStoreStrategy_CheckContextDataAsync.htm)  
##  __См. также
#### Ссылки
[CardStoreStrategy - ](T_Tessa_Cards_ComponentModel_CardStoreStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
