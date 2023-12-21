# CardDeleteStrategy - класс
Стратегия по удалению карточки.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class CardDeleteStrategy : ICardDeleteStrategy
VB __Копировать
     Public NotInheritable Class CardDeleteStrategy
    	Implements ICardDeleteStrategy
C++ __Копировать
     public ref class CardDeleteStrategy sealed : ICardDeleteStrategy
F# __Копировать
     [<SealedAttribute>]
    type CardDeleteStrategy = 
        class
            interface ICardDeleteStrategy
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardDeleteStrategy
Implements
    [ICardDeleteStrategy](T_Tessa_Cards_ComponentModel_ICardDeleteStrategy.htm)
##  __Конструкторы
[CardDeleteStrategy](M_Tessa_Cards_ComponentModel_CardDeleteStrategy__ctor.htm)|
Создаёт экземпляр класса с указанием стратегий, требуемых для удаления
карточки, и области видимости объекта
[DbManager](T_Tessa_Platform_Data_DbManager.htm).  
---|---  
## __Свойства
[TransactionStrategy](P_Tessa_Cards_ComponentModel_CardDeleteStrategy_TransactionStrategy.htm)|
Стратегия обеспечения блокировок и выполнения транзакций, используемая
сервисом.  
---|---  
##  __Методы
[DeleteAsync(CardDeleteContext)](M_Tessa_Cards_ComponentModel_CardDeleteStrategy_DeleteAsync_1.htm)|
Удаляет карточку по данным, указанным в контексте операции.  
---|---  
[DeleteAsync(Guid, CardDeletionMode, ICardMetadata, IValidationResultBuilder,
Nullable<Guid>, String, Boolean,
CancellationToken)](M_Tessa_Cards_ComponentModel_CardDeleteStrategy_DeleteAsync.htm)|
Удаляет карточку по заданным параметрам. Возвращает тип удаляемой карточки и
список ссылок на контенты файлов для удаления; эти объекты равны null, если
тип определить не удалось и удаление не было выполнено.  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
