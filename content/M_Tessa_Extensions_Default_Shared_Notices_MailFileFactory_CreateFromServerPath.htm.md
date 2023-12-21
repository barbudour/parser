# MailFileFactory.CreateFromServerPath - метод
Создаёт файл, который может прикладываться к письму и который доступен по
заданному пути на сервере, на котором установлен Chronos. После успешной
отправки файл может быть удалён в зависимости от настройки
[MailFileRemovalType](T_Tessa_Extensions_Default_Shared_Notices_MailFileRemovalType.htm).
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Notices](N_Tessa_Extensions_Default_Shared_Notices.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static MailFile CreateFromServerPath(
    	string filePath,
    	MailFileRemovalType removalType = MailFileRemovalType.KeepFile
    )
VB __Копировать
     Public Shared Function CreateFromServerPath ( 
    	filePath As String,
    	Optional removalType As MailFileRemovalType = MailFileRemovalType.KeepFile
    ) As MailFile
C++ __Копировать
     public:
    static MailFile^ CreateFromServerPath(
    	String^ filePath, 
    	MailFileRemovalType removalType = MailFileRemovalType::KeepFile
    )
F# __Копировать
     static member CreateFromServerPath : 
            filePath : string * 
            ?removalType : MailFileRemovalType 
    (* Defaults:
            let _removalType = defaultArg removalType MailFileRemovalType.KeepFile
    *)
    -> MailFile 
#### Параметры
filePath [String](https://learn.microsoft.com/dotnet/api/system.string)
    Путь к файлу на сервере (полный путь на диске или UNC-путь).
removalType
[MailFileRemovalType](T_Tessa_Extensions_Default_Shared_Notices_MailFileRemovalType.htm)
(Optional)
    Тип удаления файла после успешной отправки письма.
#### Возвращаемое значение
[MailFile](T_Tessa_Notices_MailFile.htm)  
Файл, который может прикладываться к письму и который доступен по заданному
пути на сервере, на котором установлен Chronos.
## __См. также
#### Ссылки
[MailFileFactory -
](T_Tessa_Extensions_Default_Shared_Notices_MailFileFactory.htm)
[Tessa.Extensions.Default.Shared.Notices - пространство
имён](N_Tessa_Extensions_Default_Shared_Notices.htm)
