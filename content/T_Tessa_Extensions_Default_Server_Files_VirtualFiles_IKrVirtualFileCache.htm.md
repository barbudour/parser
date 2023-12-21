# IKrVirtualFileCache - интерфейс
Кеш виртуальных файлов
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Files.VirtualFiles](N_Tessa_Extensions_Default_Server_Files_VirtualFiles.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IKrVirtualFileCache
VB __Копировать
     Public Interface IKrVirtualFileCache
C++ __Копировать
     public interface class IKrVirtualFileCache
F# __Копировать
     type IKrVirtualFileCache = interface end
##  __Методы
[GetAllAsync](M_Tessa_Extensions_Default_Server_Files_VirtualFiles_IKrVirtualFileCache_GetAllAsync.htm)|
Метод для получения всех виртуальных файлов из кеша. Загружает данные из базы
при первом вызове.  
---|---  
[GetAllowedTypesAsync](M_Tessa_Extensions_Default_Server_Files_VirtualFiles_IKrVirtualFileCache_GetAllowedTypesAsync.htm)|
Метод для получения списка идентификаторов типов карточек, которые могут иметь
виртуальные файлы  
[InvalidateAsync](M_Tessa_Extensions_Default_Server_Files_VirtualFiles_IKrVirtualFileCache_InvalidateAsync.htm)|
Метод для сброса кеша виртуальных файлов  
[TryGetAsync](M_Tessa_Extensions_Default_Server_Files_VirtualFiles_IKrVirtualFileCache_TryGetAsync.htm)|
Метод для получения виртуального файла по его ID. Загружает данные из базы при
первом вызове. Если файл отсутствует по идентификатору, то возвращает null.  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Files.VirtualFiles - пространство
имён](N_Tessa_Extensions_Default_Server_Files_VirtualFiles.htm)
