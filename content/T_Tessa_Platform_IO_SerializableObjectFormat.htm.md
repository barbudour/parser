# SerializableObjectFormat - перечисление
Формат сериализации для объектов
[SerializableObjectReader](T_Tessa_Platform_IO_SerializableObjectReader.htm) и
[SerializableObjectWriter](T_Tessa_Platform_IO_SerializableObjectWriter.htm).
## __Definition
 **Пространство имён:** [Tessa.Platform.IO](N_Tessa_Platform_IO.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public enum SerializableObjectFormat
VB __Копировать
     Public Enumeration SerializableObjectFormat
C++ __Копировать
     public enum class SerializableObjectFormat
F# __Копировать
     type SerializableObjectFormat
##  __Члены
Binary| 0|  Бинарная сериализация BSON (Tessa.Json.Bson).  
---|---|---  
Json| 1|  Текстовая сериализация Json, не использующая информацию о типах
данных всех полей. При чтении такого объекта в .NET будет утеряна информация
по типам данных, которые не специализируются в Json: Guid, Int32 и др.
Используйте TypedJson, чтобы не потерять информацию по типам при передаче из
клиента .NET в сервер .NET и обратно.  
TypedJson| 2|  Текстовая сериализация Json, сохраняющая информацию о типах
всех полей. Рекомендуется при передаче из клиента .NET в сервер .NET и
обратно.  
## __См. также
#### Ссылки
[Tessa.Platform.IO - пространство имён](N_Tessa_Platform_IO.htm)
