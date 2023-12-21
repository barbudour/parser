# CardTaskDialogHelper.PrepareFilesInSettingsDialogCardForStore - метод
Подготавливает файлы карточки диалога с временем жизни
[Settings](T_Tessa_Cards_CardTaskDialogStoreMode.htm) к сохранению.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void PrepareFilesInSettingsDialogCardForStore(
    	ICardFileContainer mainCardFileContainer,
    	Card dialogCard,
    	IFileContainer? dialogFileContainer,
    	Guid taskID,
    	Guid fileSatelliteID,
    	bool keepFiles,
    	ISession session
    )
VB __Копировать
     Public Shared Sub PrepareFilesInSettingsDialogCardForStore ( 
    	mainCardFileContainer As ICardFileContainer,
    	dialogCard As Card,
    	dialogFileContainer As IFileContainer,
    	taskID As Guid,
    	fileSatelliteID As Guid,
    	keepFiles As Boolean,
    	session As ISession
    )
C++ __Копировать
     public:
    static void PrepareFilesInSettingsDialogCardForStore(
    	ICardFileContainer^ mainCardFileContainer, 
    	Card^ dialogCard, 
    	IFileContainer^ dialogFileContainer, 
    	Guid taskID, 
    	Guid fileSatelliteID, 
    	bool keepFiles, 
    	ISession^ session
    )
F# __Копировать
     static member PrepareFilesInSettingsDialogCardForStore : 
            mainCardFileContainer : ICardFileContainer * 
            dialogCard : Card * 
            dialogFileContainer : IFileContainer * 
            taskID : Guid * 
            fileSatelliteID : Guid * 
            keepFiles : bool * 
            session : ISession -> unit 
#### Параметры
mainCardFileContainer
[ICardFileContainer](T_Tessa_Cards_ICardFileContainer.htm)
    Контейнер, содержащий информацию по основной карточке и её файлам.
dialogCard [Card](T_Tessa_Cards_Card.htm)
    Карточка диалога.
dialogFileContainer [IFileContainer](T_Tessa_Files_IFileContainer.htm)
    Контейнер, содержащий информацию по файлам диалога.
taskID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор задания диалога.
fileSatelliteID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор карточки файлового сателлита в котором должны быть сохранены файлы, расположенные в карточке диалога.
keepFiles [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
    Значение true, если необходимо сохранить файлы после завершения диалога, иначе - false.
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
Сессия пользователя.
## __См. также
#### Ссылки
[CardTaskDialogHelper - ](T_Tessa_Cards_CardTaskDialogHelper.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
