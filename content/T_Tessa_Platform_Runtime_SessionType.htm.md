# SessionType - перечисление
Тип сессии, определяющей место выполнения кода.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public enum SessionType
VB __Копировать
     Public Enumeration SessionType
C++ __Копировать
     public enum class SessionType
F# __Копировать
     type SessionType
##  __Члены
Unknown| 0|  Место выполнения кода неизвестно. Обычно это некорректное
значение для типа существующей сессии. Значение может использоваться в
атрибутах регистраторов, которые должны выполняться и на клиенте, и на сервере
(по умолчанию).  
---|---|---  
Client| 1|  Код выполняется на клиенте.  
Server| 2|  Код выполняется на сервере.  
## __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
