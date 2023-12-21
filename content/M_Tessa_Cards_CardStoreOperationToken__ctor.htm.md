# CardStoreOperationToken - конструктор
Создаёт экземпляр класса с указанием асинхронной операции по сохранению
карточки с файлами и режима её выполнения.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardStoreOperationToken(
    	CardStoreOperationMode mode,
    	Task<CardStoreResponse> task
    )
VB __Копировать
     Public Sub New ( 
    	mode As CardStoreOperationMode,
    	task As Task(Of CardStoreResponse)
    )
C++ __Копировать
     public:
    CardStoreOperationToken(
    	CardStoreOperationMode mode, 
    	Task<CardStoreResponse^>^ task
    )
F# __Копировать
     new : 
            mode : CardStoreOperationMode * 
            task : Task<CardStoreResponse> -> CardStoreOperationToken
#### Параметры
mode [CardStoreOperationMode](T_Tessa_Cards_CardStoreOperationMode.htm)
    Режим выполнения операции.
task
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[CardStoreResponse](T_Tessa_Cards_CardStoreResponse.htm)>
    Асинхронная операция по сохранению карточки с файлами.
##  __См. также
#### Ссылки
[CardStoreOperationToken - ](T_Tessa_Cards_CardStoreOperationToken.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
