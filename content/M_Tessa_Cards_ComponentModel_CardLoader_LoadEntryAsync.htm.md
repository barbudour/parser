# CardLoader.LoadEntryAsync - метод
Выполняет загрузку заданной физической строковой секции карточки, если её
загрузка разрешена.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task LoadEntryAsync(
    	CardGetContext context,
    	CardLoaderSectionInfo sectionInfo,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function LoadEntryAsync ( 
    	context As CardGetContext,
    	sectionInfo As CardLoaderSectionInfo,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    static Task^ LoadEntryAsync(
    	CardGetContext^ context, 
    	CardLoaderSectionInfo^ sectionInfo, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member LoadEntryAsync : 
            context : CardGetContext * 
            sectionInfo : CardLoaderSectionInfo * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
context [CardGetContext](T_Tessa_Cards_ComponentModel_CardGetContext.htm)
    Контекст операции по загрузке карточки.
sectionInfo
[CardLoaderSectionInfo](T_Tessa_Cards_ComponentModel_CardLoaderSectionInfo.htm)
    Информация по загружаемой строковой секции карточки.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
##  __См. также
#### Ссылки
[CardLoader - ](T_Tessa_Cards_ComponentModel_CardLoader.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
