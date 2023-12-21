# FileConverterContext.Operation - свойство
Операция, в рамках которой выполняется конвертация, или null, если операция
неизвестна или отсутствует. Из операции можно получить информацию по тому,
какой сотрудник создал запрос на конвертацию, и, например, в соответствии с
этим локализовать сообщения.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public IOperation Operation { get; }
VB __Копировать
     Public ReadOnly Property Operation As IOperation
    	Get
C++ __Копировать
     public:
    virtual property IOperation^ Operation {
    	IOperation^ get () sealed;
    }
F# __Копировать
     abstract Operation : IOperation with get
    override Operation : IOperation with get
#### Значение свойства
[IOperation](T_Tessa_Platform_Operations_IOperation.htm)
#### Реализации
[IFileConverterContext.Operation](P_Tessa_FileConverters_IFileConverterContext_Operation.htm)  
##  __См. также
#### Ссылки
[FileConverterContext - ](T_Tessa_FileConverters_FileConverterContext.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
