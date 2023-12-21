# State - перечисление
Состояния, которые может принимать узел в дереве слияния.
## __Definition
 **Пространство имён:** [Tessa.SmartMerge](N_Tessa_SmartMerge.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public enum State
VB __Копировать
     Public Enumeration State
C++ __Копировать
     public enum class State
F# __Копировать
     type State
##  __Члены
NotVisited| 0|  Узел не был посещён.  
---|---|---  
NotModified| 1|  Узел остаётся неизменным.  
Modified| 2|  Узел будет изменён.  
Inserted| 3|  Узел будет добавлен.  
Deleted| 4|  Узел будет удалён.  
Ignored| 5|  Узел игнорирован при объединении.  
Duplicated| 6|  Узел является дубликатом при объединении.  
## __См. также
#### Ссылки
[Tessa.SmartMerge - пространство имён](N_Tessa_SmartMerge.htm)
