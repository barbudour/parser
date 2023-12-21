# ICardExternalSourceLogic - интерфейс
Сущность отвечает за логику чтения и записи карточек с учетом прикрепленных
файлов и внешнего storage-контента.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardExternalSourceLogic
VB __Копировать
     Public Interface ICardExternalSourceLogic
C++ __Копировать
     public interface class ICardExternalSourceLogic
F# __Копировать
     type ICardExternalSourceLogic = interface end
##  __Методы
[CheckFilesInSubDirectoryAsync](M_Tessa_Cards_ICardExternalSourceLogic_CheckFilesInSubDirectoryAsync.htm)|
Логика проверки файлов в поддиректории карточки.  
---|---  
[GetSpecialFileNames](M_Tessa_Cards_ICardExternalSourceLogic_GetSpecialFileNames.htm)|
Получает имена специальных файлов, которые могут находиться в поддиректории
карточки.  
[ParseBinaryCardAsync](M_Tessa_Cards_ICardExternalSourceLogic_ParseBinaryCardAsync.htm)|
Парсинг карточки в Binary формате.  
[ParseJsonCardAsync](M_Tessa_Cards_ICardExternalSourceLogic_ParseJsonCardAsync.htm)|
Парсинг карточки в формате Json.  
[ReadCardAsync](M_Tessa_Cards_ICardExternalSourceLogic_ReadCardAsync.htm)|
Чтение карточки.  
[ReadJsonCardAsync](M_Tessa_Cards_ICardExternalSourceLogic_ReadJsonCardAsync.htm)|
Чтение Json карточки.  
[WriteBinaryCardAsync](M_Tessa_Cards_ICardExternalSourceLogic_WriteBinaryCardAsync.htm)|
Запись карточки в Binary формате.  
[WriteJsonCardAsync](M_Tessa_Cards_ICardExternalSourceLogic_WriteJsonCardAsync.htm)|
Запись карточки в формате Json.  
## __См. также
#### Ссылки
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
