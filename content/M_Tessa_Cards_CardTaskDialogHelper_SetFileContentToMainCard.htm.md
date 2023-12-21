# CardTaskDialogHelper.SetFileContentToMainCard - метод
Задаёт контент указанных файлов в основную карточку.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetFileContentToMainCard(
    	Card dialogCard,
    	Guid dialogTaskID,
    	IReadOnlyCollection<IFile> dialogFiles,
    	Card mainCard,
    	IFileContainer mainCardFileContainer,
    	ISession session
    )
VB __Копировать
     Public Shared Sub SetFileContentToMainCard ( 
    	dialogCard As Card,
    	dialogTaskID As Guid,
    	dialogFiles As IReadOnlyCollection(Of IFile),
    	mainCard As Card,
    	mainCardFileContainer As IFileContainer,
    	session As ISession
    )
C++ __Копировать
     public:
    static void SetFileContentToMainCard(
    	Card^ dialogCard, 
    	Guid dialogTaskID, 
    	IReadOnlyCollection<IFile^>^ dialogFiles, 
    	Card^ mainCard, 
    	IFileContainer^ mainCardFileContainer, 
    	ISession^ session
    )
F# __Копировать
     static member SetFileContentToMainCard : 
            dialogCard : Card * 
            dialogTaskID : Guid * 
            dialogFiles : IReadOnlyCollection<IFile> * 
            mainCard : Card * 
            mainCardFileContainer : IFileContainer * 
            session : ISession -> unit 
#### Параметры
dialogCard [Card](T_Tessa_Cards_Card.htm)
    Карточка диалога.
dialogTaskID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор задания, к которому относится диалог.
dialogFiles
[IReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlycollection-1)<[IFile](T_Tessa_Files_IFile.htm)>
    Коллекция файлов, содержащийся в карточке диалога.
mainCard [Card](T_Tessa_Cards_Card.htm)
    Основная карточка.
mainCardFileContainer [IFileContainer](T_Tessa_Files_IFileContainer.htm)
    Контейнер, содержащий файлы основной карточки.
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
Сессия пользователя.
## __См. также
#### Ссылки
[CardTaskDialogHelper - ](T_Tessa_Cards_CardTaskDialogHelper.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
