# CreateFileSourceForCardFuncAsync - делегат
Создаёт источник файлов для заданной карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public delegate ValueTask<FileSourceForCard> CreateFileSourceForCardFuncAsync(
    	Card card,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Delegate Function CreateFileSourceForCardFuncAsync ( 
    	card As Card,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of FileSourceForCard)
C++ __Копировать
     public delegate ValueTask<FileSourceForCard^> CreateFileSourceForCardFuncAsync(
    	Card^ card, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     type CreateFileSourceForCardFuncAsync = 
        delegate of 
            card : Card * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<FileSourceForCard>
#### Параметры
card [Card](T_Tessa_Cards_Card.htm)
    Карточка, по данным которой создаётся источник файлов.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[FileSourceForCard](T_Tessa_Cards_FileSourceForCard.htm)>  
Созданный источник файлов.
##  __См. также
#### Ссылки
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
