# INumberObjectManager - интерфейс
Объект, определяющий поведение объекта
[INumberObject](T_Tessa_Cards_Numbers_INumberObject.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface INumberObjectManager : INumberLocationManager
VB __Копировать
     Public Interface INumberObjectManager
    	Inherits INumberLocationManager
C++ __Копировать
     public interface class INumberObjectManager : INumberLocationManager
F# __Копировать
     type INumberObjectManager = 
        interface
            interface INumberLocationManager
        end
Implements
    [INumberLocationManager](T_Tessa_Cards_Numbers_INumberLocationManager.htm)
##  __Методы
[GetNumberAsync](M_Tessa_Cards_Numbers_INumberLocationManager_GetNumberAsync.htm)|
Возвращает номер, расположенный в заданных местоположении и контексте или
пустой номер, если он не был найден. Метод не возвращает null.  
(Унаследован от
[INumberLocationManager](T_Tessa_Cards_Numbers_INumberLocationManager.htm))  
---|---  
[StoreNumberAsync(INumberContext, INumberObject, NumberStoreMode,
CancellationToken)](M_Tessa_Cards_Numbers_INumberObjectManager_StoreNumberAsync.htm)|
Сохраняет объект с номером в контексте и по местоположению, определяемому его
типом.  
[StoreNumberAsync(INumberContext, INumberObject, INumberLocation,
NumberStoreMode,
CancellationToken)](M_Tessa_Cards_Numbers_INumberLocationManager_StoreNumberAsync.htm)|
Сохраняет объект с номером в заданном местоположении и контексте.  
(Унаследован от
[INumberLocationManager](T_Tessa_Cards_Numbers_INumberLocationManager.htm))  
##  __Методы расширения
[GetNumberAsync](M_Tessa_Cards_Numbers_NumberExtensions_GetNumberAsync_1.htm)|
Возвращает номер, расположенный в заданных местоположении и контексте или
пустой номер, если он не был найден. Метод не возвращает null.  
(Определяется [NumberExtensions](T_Tessa_Cards_Numbers_NumberExtensions.htm))  
---|---  
##  __См. также
#### Ссылки
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
