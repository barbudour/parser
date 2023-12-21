# FileSourceForCard.GetFileCreationTokenCoreAsync - метод
Создаёт токен, используемый для создания файлов посредством источника файлов
[IFileSource].
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected override ValueTask<IFileCreationToken> GetFileCreationTokenCoreAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected Overrides Function GetFileCreationTokenCoreAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of IFileCreationToken)
C++ __Копировать
     protected:
    virtual ValueTask<IFileCreationToken^> GetFileCreationTokenCoreAsync(
    	CancellationToken cancellationToken = CancellationToken()
    ) override
F# __Копировать
     abstract GetFileCreationTokenCoreAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IFileCreationToken> 
    override GetFileCreationTokenCoreAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IFileCreationToken> 
#### Параметры
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[IFileCreationToken](T_Tessa_Files_IFileCreationToken.htm)>  
Токен, используемый для создания файлов посредством источника файлов
[IFileSource].
## __Заметки
По умолчанию создаётся токен с указанием стандартного типа файла, полученного
вызовом метода [CreateDefaultAsync(ICardMetadata,
CancellationToken)](M_Tessa_Cards_CardFileType_CreateDefaultAsync.htm).
## __См. также
#### Ссылки
[FileSourceForCard - ](T_Tessa_Cards_FileSourceForCard.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
