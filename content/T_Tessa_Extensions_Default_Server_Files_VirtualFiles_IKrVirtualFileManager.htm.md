# IKrVirtualFileManager - интерфейс
Объект для получения информации о виртуальных файлах по карточке и проверки
доступа к файлам.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Files.VirtualFiles](N_Tessa_Extensions_Default_Server_Files_VirtualFiles.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IKrVirtualFileManager
VB __Копировать
     Public Interface IKrVirtualFileManager
C++ __Копировать
     public interface class IKrVirtualFileManager
F# __Копировать
     type IKrVirtualFileManager = interface end
##  __Методы
[CheckAccessForFileAsync](M_Tessa_Extensions_Default_Server_Files_VirtualFiles_IKrVirtualFileManager_CheckAccessForFileAsync.htm)|
Метод для проверки доступа на виртуальный файл для карточки.  
---|---  
[FillCardWithFilesAsync](M_Tessa_Extensions_Default_Server_Files_VirtualFiles_IKrVirtualFileManager_FillCardWithFilesAsync.htm)|
Метод для установки виртуальных файлов в карточку с учетом проверок доступа.
Возвращает результат выполнения, в котором могут быть сообщения об ошибках.  
[GetSuggestedFileNameAsync](M_Tessa_Extensions_Default_Server_Files_VirtualFiles_IKrVirtualFileManager_GetSuggestedFileNameAsync.htm)|
Возвращает предпочитаемое имя файла, сгенерированного по версии файла из
шаблона. При этом заменяются плейсхолдеры в заданном шаблонизированном имени
templateFileName.  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Files.VirtualFiles - пространство
имён](N_Tessa_Extensions_Default_Server_Files_VirtualFiles.htm)
