# ICardPermissionResolver - интерфейс
Осуществляет поиск прав доступа для полей, строк, файлов и карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardPermissionResolver
VB __Копировать
     Public Interface ICardPermissionResolver
C++ __Копировать
     public interface class ICardPermissionResolver
F# __Копировать
     type ICardPermissionResolver = interface end
##  __Методы
[GetCardPermissions](M_Tessa_Cards_ICardPermissionResolver_GetCardPermissions.htm)|
Возвращает права доступа к карточке.  
---|---  
[GetFieldPermissions(String,
String)](M_Tessa_Cards_ICardPermissionResolver_GetFieldPermissions.htm)|
Возвращает права доступа к полю fieldName из секции sectionName.  
[GetFieldPermissions(String, String,
Guid)](M_Tessa_Cards_ICardPermissionResolver_GetFieldPermissions_1.htm)|
Возвращает права доступа к полю fieldName из коллекционной или древовидной
секции sectionName и строки с идентификатором rowID.  
[GetFilePermissions](M_Tessa_Cards_ICardPermissionResolver_GetFilePermissions.htm)|
Возвращает права доступа к прикреплённому к карточке файлу fileID.  
[GetRowPermissions](M_Tessa_Cards_ICardPermissionResolver_GetRowPermissions.htm)|
Возвращает права доступа к строке с идентификатором rowID из секции
sectionName.  
[GetSectionPermissions](M_Tessa_Cards_ICardPermissionResolver_GetSectionPermissions.htm)|
Возвращает права доступа к строкам или полям секции sectionName.  
[Invalidate](M_Tessa_Cards_ICardPermissionResolver_Invalidate.htm)|
Очищает кэш прав доступа.
Метод необходимо вызывать всякий раз перед поиском прав доступа, если нет
уверенности в неизменности прав доступа после предыдущего поиска.  
## __Методы расширения
[GetEntryPermissions](M_Tessa_Cards_CardExtensions_GetEntryPermissions.htm)|
Возвращает права доступа к полям строковой секции с именем sectionName.  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
---|---  
[GetTablePermissions](M_Tessa_Cards_CardExtensions_GetTablePermissions.htm)|
Возвращает права доступа к строкам коллекционной секции с именем sectionName.  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
