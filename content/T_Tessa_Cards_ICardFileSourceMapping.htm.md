# ICardFileSourceMapping - интерфейс
Отображение между источниками контента для файлов одной и той же карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardFileSourceMapping : ISealable
VB __Копировать
     Public Interface ICardFileSourceMapping
    	Inherits ISealable
C++ __Копировать
     public interface class ICardFileSourceMapping : ISealable
F# __Копировать
     type ICardFileSourceMapping = 
        interface
            interface ISealable
        end
Implements
    [ISealable](T_Tessa_Platform_ISealable.htm)
##  __Свойства
[IsSealed](P_Tessa_Platform_ISealable_IsSealed.htm)| Признак того, что объект
был защищён от изменений.  
(Унаследован от [ISealable](T_Tessa_Platform_ISealable.htm))  
---|---  
##  __Методы
[CreateContentSource](M_Tessa_Cards_ICardFileSourceMapping_CreateContentSource.htm)|
Создаёт источник контента файла, который можно использовать в отображении без
потерь в производительности.  
---|---  
[Map](M_Tessa_Cards_ICardFileSourceMapping_Map.htm)|  Создаёт отображение
между файлом с заданными параметрами отображения и указанным объектом
источника контента файла.  
[Seal](M_Tessa_Platform_ISealable_Seal.htm)| Защищает объект от изменений.  
(Унаследован от [ISealable](T_Tessa_Platform_ISealable.htm))  
[TryGet](M_Tessa_Cards_ICardFileSourceMapping_TryGet.htm)|  Возвращает
источник контента файла для заданных параметров отображения или null, если
отображение не найдено.  
## __См. также
#### Ссылки
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
