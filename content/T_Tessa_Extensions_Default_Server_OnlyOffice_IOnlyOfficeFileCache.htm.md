# IOnlyOfficeFileCache - интерфейс
Кэш файлов, используемый для взаимодействия с OnlyOffice.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.OnlyOffice](N_Tessa_Extensions_Default_Server_OnlyOffice.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IOnlyOfficeFileCache
VB __Копировать
     Public Interface IOnlyOfficeFileCache
C++ __Копировать
     public interface class IOnlyOfficeFileCache
F# __Копировать
     type IOnlyOfficeFileCache = interface end
##  __Методы
[CreateAsync](M_Tessa_Extensions_Default_Server_OnlyOffice_IOnlyOfficeFileCache_CreateAsync.htm)|
Сохраняет содержимое нового файла в кэш.  
---|---  
[DeleteAsync](M_Tessa_Extensions_Default_Server_OnlyOffice_IOnlyOfficeFileCache_DeleteAsync.htm)|
Удаляет содержимое файла из кэша по указанному идентификатору. Выбрасывает
исключение, если файл не найден в кэше.  
[GetContentAsync](M_Tessa_Extensions_Default_Server_OnlyOffice_IOnlyOfficeFileCache_GetContentAsync.htm)|
Возвращает содержимое файла из кэша. Выбрасывает исключение, если файл не
найден в кэше.  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.OnlyOffice - пространство
имён](N_Tessa_Extensions_Default_Server_OnlyOffice.htm)
