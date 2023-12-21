# ICardRequestComponent - интерфейс
Компонент, выполняющий универсальный запрос к сервису карточек.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardRequestComponent
VB __Копировать
     Public Interface ICardRequestComponent
C++ __Копировать
     public interface class ICardRequestComponent
F# __Копировать
     type ICardRequestComponent = interface end
##  __Методы
[RequestAsync](M_Tessa_Cards_ComponentModel_ICardRequestComponent_RequestAsync.htm)|
Выполняет универсальный запрос к сервису карточек.  
---|---  
##  __Методы расширения
[GetFileSourceAsync](M_Tessa_Cards_CardExtensions_GetFileSourceAsync.htm)|
Возвращает местоположение контента файла для заданного файла file указанной
карточки card. Местоположение определяется выполнением запроса
[GetFileSource](F_Tessa_Cards_CardRequestTypes_GetFileSource.htm). Метод
возвращает null, если определить местоположение не удалось, обычно в этом
случае будет использоваться местоположение по умолчанию.  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
---|---  
##  __См. также
#### Ссылки
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
