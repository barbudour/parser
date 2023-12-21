# FileSourceForCard.NotifyCoreAsync(IFile, FileNotificationType,
CancellationToken) - метод
Уведомляет подсистему о том, что с файлом было произведено указанное действие.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected override ValueTask NotifyCoreAsync(
    	IFile file,
    	FileNotificationType notificationType,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected Overrides Function NotifyCoreAsync ( 
    	file As IFile,
    	notificationType As FileNotificationType,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask
C++ __Копировать
     protected:
    virtual ValueTask NotifyCoreAsync(
    	IFile^ file, 
    	FileNotificationType notificationType, 
    	CancellationToken cancellationToken = CancellationToken()
    ) override
F# __Копировать
     abstract NotifyCoreAsync : 
            file : IFile * 
            notificationType : FileNotificationType * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask 
    override NotifyCoreAsync : 
            file : IFile * 
            notificationType : FileNotificationType * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask 
#### Параметры
file [IFile](T_Tessa_Files_IFile.htm)
    Файл, с которым произведено указанное действие.
notificationType
[FileNotificationType](T_Tessa_Files_FileNotificationType.htm)
    Тип события, которое отражает действие, произошедшее с файлом.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)  
Асинхронная задача.
##  __См. также
#### Ссылки
[FileSourceForCard - ](T_Tessa_Cards_FileSourceForCard.htm)
[NotifyCoreAsync -
перегрузка](Overload_Tessa_Cards_FileSourceForCard_NotifyCoreAsync.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
