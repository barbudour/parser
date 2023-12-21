# IValidationResultItem - интерфейс
Сообщение о валидации.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Validation](N_Tessa_Platform_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IValidationResultItem : IEquatable<IValidationResultItem>
VB __Копировать
     Public Interface IValidationResultItem
    	Inherits IEquatable(Of IValidationResultItem)
C++ __Копировать
     public interface class IValidationResultItem : IEquatable<IValidationResultItem^>
F# __Копировать
     type IValidationResultItem = 
        interface
            interface IEquatable<IValidationResultItem>
        end
Implements
    [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<IValidationResultItem>
##  __Свойства
[Details](P_Tessa_Platform_Validation_IValidationResultItem_Details.htm)|
Дополнительная информация о сообщении, например, полный текст исключения, или
null, если дополнительная информация отсутствует.  
---|---  
[FieldName](P_Tessa_Platform_Validation_IValidationResultItem_FieldName.htm)|
Имя поля объекта, к которому относится сообщение валидации, или null, если
поле неизвестно.  
[Key](P_Tessa_Platform_Validation_IValidationResultItem_Key.htm)| Ключ
сообщения, возникшего при валидации.  
[Message](P_Tessa_Platform_Validation_IValidationResultItem_Message.htm)|
Текст сообщения, возникшего при валидации.  
[ObjectName](P_Tessa_Platform_Validation_IValidationResultItem_ObjectName.htm)|
Имя объекта, к которому относится сообщение валидации, или null, если имя
неизвестно.  
[ObjectType](P_Tessa_Platform_Validation_IValidationResultItem_ObjectType.htm)|
Тип объекта, к которому относится сообщение валидации, или null, если тип
неизвестен.  
[Type](P_Tessa_Platform_Validation_IValidationResultItem_Type.htm)| Тип
сообщения, возникшего при валидации.  
##  __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.iequatable-1.equals#system-
iequatable-1-equals\(-0\))| Indicates whether the current object is equal to
another object of the same type.  
(Унаследован от
[IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<IValidationResultItem>)  
---|---  
##  __См. также
#### Ссылки
[Tessa.Platform.Validation - пространство
имён](N_Tessa_Platform_Validation.htm)
