# INumberLocation - интерфейс
Информация по местоположению номера в карточке или в контексте события,
происходящего с номером.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface INumberLocation : ISealable
VB __Копировать
     Public Interface INumberLocation
    	Inherits ISealable
C++ __Копировать
     public interface class INumberLocation : ISealable
F# __Копировать
     type INumberLocation = 
        interface
            interface ISealable
        end
Implements
    [ISealable](T_Tessa_Platform_ISealable.htm)
##  __Свойства
[Info](P_Tessa_Cards_Numbers_INumberLocation_Info.htm)| Дополнительная
информация, связанная с местоположением номера.  
---|---  
[IsSealed](P_Tessa_Platform_ISealable_IsSealed.htm)| Признак того, что объект
был защищён от изменений.  
(Унаследован от [ISealable](T_Tessa_Platform_ISealable.htm))  
[Manager](P_Tessa_Cards_Numbers_INumberLocation_Manager.htm)| Объект,
определяющий поведение текущего объекта.  
[Type](P_Tessa_Cards_Numbers_INumberLocation_Type.htm)| Тип расположения
номера (в карточке или в контексте события, происходящего с номером).  
##  __Методы
[Seal](M_Tessa_Platform_ISealable_Seal.htm)| Защищает объект от изменений.  
(Унаследован от [ISealable](T_Tessa_Platform_ISealable.htm))  
---|---  
##  __Методы расширения
[GetNumberAsync](M_Tessa_Cards_Numbers_NumberExtensions_GetNumberAsync.htm)|
Возвращает номер, расположенный в заданных местоположении и контексте или
пустой номер, если он не был найден. Метод не возвращает null.  
(Определяется [NumberExtensions](T_Tessa_Cards_Numbers_NumberExtensions.htm))  
---|---  
[StoreNumberAsync](M_Tessa_Cards_Numbers_NumberExtensions_StoreNumberAsync.htm)|
Сохраняет объект с номером в заданном местоположении и контексте.  
(Определяется [NumberExtensions](T_Tessa_Cards_Numbers_NumberExtensions.htm))  
[ToCardNumberLocation](M_Tessa_Cards_Numbers_NumberExtensions_ToCardNumberLocation.htm)|
Преобразует местоположение номера INumberLocation типа
[Card](F_Tessa_Cards_Numbers_NumberLocationTypes_Card.htm) в объект
[CardNumberLocation](T_Tessa_Cards_Numbers_CardNumberLocation.htm). Может
вернуть null, если преобразование не удалось.  
(Определяется [NumberExtensions](T_Tessa_Cards_Numbers_NumberExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
