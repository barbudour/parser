# ICardFileVersionStrategy - интерфейс
Стратегия, загружающая информацию по версиям файла и устанавливающая состояние
версии файла.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardFileVersionStrategy
VB __Копировать
     Public Interface ICardFileVersionStrategy
C++ __Копировать
     public interface class ICardFileVersionStrategy
F# __Копировать
     type ICardFileVersionStrategy = interface end
##  __Методы
[GetVersionAsync](M_Tessa_Cards_ComponentModel_ICardFileVersionStrategy_GetVersionAsync.htm)|
Возвращает общую информацию по версии файла с заданным идентификатором.  
---|---  
[GetVersionsAsync](M_Tessa_Cards_ComponentModel_ICardFileVersionStrategy_GetVersionsAsync.htm)|
Возвращает список с общей информацией по версиям файла с заданным
идентификатором.  
[SetUploadErrorAsync](M_Tessa_Cards_ComponentModel_ICardFileVersionStrategy_SetUploadErrorAsync.htm)|
Устанавливает, что загрузка контента для версии файла с заданным
идентификатором произошла с ошибкой.  
[SetUploadSuccessfulAsync](M_Tessa_Cards_ComponentModel_ICardFileVersionStrategy_SetUploadSuccessfulAsync.htm)|
Устанавливает, что загрузка контента для версии файла с заданным
идентификатором была успешно завершена.  
[TryGetContentHashAsync](M_Tessa_Cards_ComponentModel_ICardFileVersionStrategy_TryGetContentHashAsync.htm)|
Возвращает хеш контента для версии файла с заданным идентификатором. Хеш может
быть равен null, если версия не найдена или её хеш не был рассчитан.  
## __См. также
#### Ссылки
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
