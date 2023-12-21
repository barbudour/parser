# ICardStreamClientRepository - интерфейс
Репозиторий для потокового управления карточками на клиенте. Репозиторий
доступен также на сервере в вариантах без расширений.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardStreamClientRepository
VB __Копировать
     Public Interface ICardStreamClientRepository
C++ __Копировать
     public interface class ICardStreamClientRepository
F# __Копировать
     type ICardStreamClientRepository = interface end
##  __Методы
[GetFileContentAsync](M_Tessa_Cards_ICardStreamClientRepository_GetFileContentAsync.htm)|
Получает контент версии файла.  
---|---  
[StoreAsync](M_Tessa_Cards_ICardStreamClientRepository_StoreAsync.htm)|
Сохраняет карточку с контентом файлов, которые упаковываются в поток карточки
перед отправкой на сервер.  
##  __Методы расширения
[GenerateExportAsync](M_Tessa_Cards_CardExtensions_GenerateExportAsync.htm)|
Создаёт файл по заданному шаблону и возвращает контент созданного файла и
ответ на запрос на создание.  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
---|---  
[GenerateFileFromTemplateAsync](M_Tessa_Cards_CardExtensions_GenerateFileFromTemplateAsync.htm)|
Создаёт файл по заданному шаблону и возвращает контент созданного файла и
ответ на запрос на создание.  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
