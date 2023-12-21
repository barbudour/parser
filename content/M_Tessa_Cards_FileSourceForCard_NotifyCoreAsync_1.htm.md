# FileSourceForCard.NotifyCoreAsync(IFileSignature,
FileSignatureNotificationType, CancellationToken) - метод
Уведомляет подсистему о том, что с подписью файла было произведено указанное
действие.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected override ValueTask NotifyCoreAsync(
    	IFileSignature signature,
    	FileSignatureNotificationType notificationType,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected Overrides Function NotifyCoreAsync ( 
    	signature As IFileSignature,
    	notificationType As FileSignatureNotificationType,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask
C++ __Копировать
     protected:
    virtual ValueTask NotifyCoreAsync(
    	IFileSignature^ signature, 
    	FileSignatureNotificationType notificationType, 
    	CancellationToken cancellationToken = CancellationToken()
    ) override
F# __Копировать
     abstract NotifyCoreAsync : 
            signature : IFileSignature * 
            notificationType : FileSignatureNotificationType * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask 
    override NotifyCoreAsync : 
            signature : IFileSignature * 
            notificationType : FileSignatureNotificationType * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask 
#### Параметры
signature [IFileSignature](T_Tessa_Files_IFileSignature.htm)
notificationType
[FileSignatureNotificationType](T_Tessa_Files_FileSignatureNotificationType.htm)
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
