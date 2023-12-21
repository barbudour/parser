# OperationCreationFlags - перечисление
Флаги, описывающие создаваемую операцию.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Operations](N_Tessa_Platform_Operations.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [DataContractAttribute]
    [FlagsAttribute]
    public enum OperationCreationFlags
VB __Копировать
    <DataContractAttribute>
    <FlagsAttribute>
    Public Enumeration OperationCreationFlags
C++ __Копировать
    [DataContractAttribute]
    [FlagsAttribute]
    public enum class OperationCreationFlags
F# __Копировать
     [<DataContractAttribute>]
    [<FlagsAttribute>]
    type OperationCreationFlags
##  __Члены
None| 0|  Операция создаётся с параметрами по умолчанию.  
---|---|---  
CreateInProgress| 1|  Операция создаётся в состоянии
[InProgress](T_Tessa_Platform_Operations_OperationState.htm). Если флаг не
указан, то операция создаётся в состоянии
[Created](T_Tessa_Platform_Operations_OperationState.htm).  
ReportsProgress| 2|  Операция сообщает процент своей готовности в поле
[Progress](P_Tessa_Platform_Operations_Operation_Progress.htm). Если флаг не
указан, то это поле возвращает null.  
FailWhenHasSameRequestHash| 4|  Создание операции запрещено и вызовет
[OperationAlreadyExistsException](T_Tessa_Platform_Operations_OperationAlreadyExistsException.htm),
если в настоящий момент выполняется операция с таким же хешом
[RequestHash](P_Tessa_Platform_Operations_IOperation_RequestHash.htm) и типом
[TypeID](P_Tessa_Platform_Operations_IOperation_TypeID.htm). Если флаг не
указан, то выполняется проверка только для наличия операции с таким же
идентификатором [ID](P_Tessa_Platform_Operations_IOperation_ID.htm).  
## __См. также
#### Ссылки
[Tessa.Platform.Operations - пространство
имён](N_Tessa_Platform_Operations.htm)
