# ISharedEventArgs - интерфейс
Аргументы события, разделяемые между процессами. Каждый подписчик получает
копию аргументов события.
## __Definition
 **Пространство имён:** [Tessa.Platform.IPC](N_Tessa_Platform_IPC.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ISharedEventArgs : IBinarySerializable
VB __Копировать
     Public Interface ISharedEventArgs
    	Inherits IBinarySerializable
C++ __Копировать
     public interface class ISharedEventArgs : IBinarySerializable
F# __Копировать
     type ISharedEventArgs = 
        interface
            interface IBinarySerializable
        end
Implements
    [IBinarySerializable](T_Tessa_Platform_IBinarySerializable.htm)
##  __Заметки
Сериализованный в бинарную форму объект хранится в разделяемой памяти, которая
имеет ограниченный объём, поэтому во избежании нарушения работы механизма
рассылки уведомлений рекомендуется сериализовать аргументы события в как можно
более компактной форме.
## __Методы
[Deserialize](M_Tessa_Platform_IBinarySerializable_Deserialize.htm)|
Десериализует объект из бинарной формы.  
(Унаследован от
[IBinarySerializable](T_Tessa_Platform_IBinarySerializable.htm))  
---|---  
[Serialize](M_Tessa_Platform_IBinarySerializable_Serialize.htm)| Сериализует
объект в бинарной форме.  
(Унаследован от
[IBinarySerializable](T_Tessa_Platform_IBinarySerializable.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform.IPC - пространство имён](N_Tessa_Platform_IPC.htm)
