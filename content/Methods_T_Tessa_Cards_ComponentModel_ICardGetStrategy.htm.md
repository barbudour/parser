# ICardGetStrategy - методы
##  __Методы
[GetTypeIDAsync](M_Tessa_Cards_ComponentModel_ICardGetStrategy_GetTypeIDAsync.htm)|
Возвращает идентификатор типа карточки, файла или задания по идентификатору
экземпляра или null, если карточка, файл или задание не найдены.  
---|---  
[GetTypeIDsAsync](M_Tessa_Cards_ComponentModel_ICardGetStrategy_GetTypeIDsAsync.htm)|
Возвращает идентификаторы типов карточек, файлов или заданий по
идентификаторам экземпляров. Порядок возвращённых идентификаторов типов
соответствует порядку переданных экземпляров instanceIDs. Возвращённый
идентификатор типа равен null, если карточка, файл или задание с
соответствующим идентификатором экземпляра не найдены.  
[LoadFileVersionsAsync](M_Tessa_Cards_ComponentModel_ICardGetStrategy_LoadFileVersionsAsync.htm)|
Загружает информацию по версиям файла.  
[LoadSectionsAsync](M_Tessa_Cards_ComponentModel_ICardGetStrategy_LoadSectionsAsync.htm)|
Загружает секции карточки.  
[LoadTaskHistoryAsync](M_Tessa_Cards_ComponentModel_ICardGetStrategy_LoadTaskHistoryAsync.htm)|
Загружает информацию по истории завершённых заданий карточки.  
[LoadTaskHistoryGroupsAsync](M_Tessa_Cards_ComponentModel_ICardGetStrategy_LoadTaskHistoryGroupsAsync.htm)|
Загружает информацию по группам истории завершённых заданий карточки.  
[TryLoadCardInstanceAsync](M_Tessa_Cards_ComponentModel_ICardGetStrategy_TryLoadCardInstanceAsync.htm)|
Загружает общую информацию по экземпляру карточки из таблицы Instances и
возвращает контекст операции или null, если загрузку произвести не удалось.  
[TryLoadFileInstancesAsync](M_Tessa_Cards_ComponentModel_ICardGetStrategy_TryLoadFileInstancesAsync.htm)|
Загружает общую информацию по экземплярам файлов, приложенных к заданной
карточке, и возвращает список контекстов операций по загрузке каждого из
файлов или null, если загрузку произвести не удалось.  
[TryLoadTaskHistoryGroupAsync](M_Tessa_Cards_ComponentModel_ICardGetStrategy_TryLoadTaskHistoryGroupAsync.htm)|
Загружает информацию по группе в истории завершённых заданий карточки.  
[TryLoadTaskHistoryItemAsync](M_Tessa_Cards_ComponentModel_ICardGetStrategy_TryLoadTaskHistoryItemAsync.htm)|
Загружает информацию по записи в истории завершённых заданий карточки.  
[TryLoadTaskInstancesAsync](M_Tessa_Cards_ComponentModel_ICardGetStrategy_TryLoadTaskInstancesAsync.htm)|
Загружает общую информацию по экземплярам заданий, приложенных к заданной
карточке, и возвращает список контекстов операций по загрузке каждого из
заданий или null, если загрузку произвести не удалось.  
## __См. также
#### Ссылки
[ICardGetStrategy - ](T_Tessa_Cards_ComponentModel_ICardGetStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
