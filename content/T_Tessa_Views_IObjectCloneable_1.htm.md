# IObjectCloneable<T> \- интерфейс
Интерфейс клонирования объекта
## __Definition
 **Пространство имён:** [Tessa.Views](N_Tessa_Views.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IObjectCloneable<out T>
    where T : IReadOnlyMarker
VB __Копировать
     Public Interface IObjectCloneable(Of Out T As IReadOnlyMarker)
C++ __Копировать
    generic<typename T>
    where T : IReadOnlyMarker
    public interface class IObjectCloneable
F# __Копировать
     type IObjectCloneable<'T when 'T : IReadOnlyMarker> = interface end
#### Параметры типа
T
     Тип данных 
## __Методы
[Clone](M_Tessa_Views_IObjectCloneable_1_Clone.htm)|  Осуществляет
клонирование объекта  
---|---  
[CloneAsReadOnly](M_Tessa_Views_IObjectCloneable_1_CloneAsReadOnly.htm)|
Осуществляет клонирование объекта с установкой свойства
[IReadOnlyMarker](T_Tessa_Views_IReadOnlyMarker.htm) в true  
##  __См. также
#### Ссылки
[Tessa.Views - пространство имён](N_Tessa_Views.htm)
