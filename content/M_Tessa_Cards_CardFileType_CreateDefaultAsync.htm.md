# CardFileType.CreateDefaultAsync - метод
Создаёт тип [IFileType](T_Tessa_Files_IFileType.htm) для стандартного файла
карточки с идентификатором
[FileTypeID](F_Tessa_Cards_CardHelper_FileTypeID.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static ValueTask<CardFileType> CreateDefaultAsync(
    	ICardMetadata cardMetadata,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function CreateDefaultAsync ( 
    	cardMetadata As ICardMetadata,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of CardFileType)
C++ __Копировать
     public:
    static ValueTask<CardFileType^> CreateDefaultAsync(
    	ICardMetadata^ cardMetadata, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member CreateDefaultAsync : 
            cardMetadata : ICardMetadata * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<CardFileType> 
#### Параметры
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
    Метаинформация по типам карточек, содержащая стандартный тип файла.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[CardFileType](T_Tessa_Cards_CardFileType.htm)>  
Созданный тип [IFileType](T_Tessa_Files_IFileType.htm), пригодный для
использования в файловом API.
##  __См. также
#### Ссылки
[CardFileType - ](T_Tessa_Cards_CardFileType.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
