# CardWriter.WriteAsync(CardStorageObject, CancellationToken) - метод
Выполняет запись сериализуемого объекта карточек в поток карточки.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task WriteAsync(
    	CardStorageObject obj,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function WriteAsync ( 
    	obj As CardStorageObject,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    Task^ WriteAsync(
    	CardStorageObject^ obj, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     member WriteAsync : 
            obj : CardStorageObject * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
obj [CardStorageObject](T_Tessa_Cards_CardStorageObject.htm)
     Сериализуемый объект карточек, который необходимо записать в поток карточки. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
##  __См. также
#### Ссылки
[CardWriter - ](T_Tessa_Cards_ComponentModel_CardWriter.htm)
[WriteAsync -
перегрузка](Overload_Tessa_Cards_ComponentModel_CardWriter_WriteAsync.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
