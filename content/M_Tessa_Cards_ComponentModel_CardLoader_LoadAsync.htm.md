# CardLoader.LoadAsync - метод
Загружает секции карточки, используя информацию из заданного объекта context.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task LoadAsync(
    	CardGetContext context,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function LoadAsync ( 
    	context As CardGetContext,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    Task^ LoadAsync(
    	CardGetContext^ context, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     member LoadAsync : 
            context : CardGetContext * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
context [CardGetContext](T_Tessa_Cards_ComponentModel_CardGetContext.htm)
    Контекст операции по загрузке карточки.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
##  __Заметки
Метод является потокобезопасным.
## __См. также
#### Ссылки
[CardLoader - ](T_Tessa_Cards_ComponentModel_CardLoader.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
