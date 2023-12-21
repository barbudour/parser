# MailFileRemovalType - перечисление
Тип удаления файла после успешной отправки письма.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Notices](N_Tessa_Extensions_Default_Shared_Notices.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public enum MailFileRemovalType
VB __Копировать
     Public Enumeration MailFileRemovalType
C++ __Копировать
     public enum class MailFileRemovalType
F# __Копировать
     type MailFileRemovalType
##  __Члены
KeepFile| 0|  Файл не удаляется.  
---|---|---  
RemoveFileOnly| 1|  Удаляется файл, но не папка, в которой расположен файл.  
RemoveFileAndFolder| 2|  Удаляется файл и папка, в которой он расположен, если
папка будет пуста после удаления файла.  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Shared.Notices - пространство
имён](N_Tessa_Extensions_Default_Shared_Notices.htm)
