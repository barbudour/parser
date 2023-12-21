# WorkflowTemplateStorageWithDescriptionBase - класс
Базовый класс для хранения объектов WorkflowEngine, относящихся к шаблону
процесса
## __Definition
 **Пространство имён:** [Tessa.Workflow.Storage](N_Tessa_Workflow_Storage.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class WorkflowTemplateStorageWithDescriptionBase : WorkflowTemplateStorageBase
VB __Копировать
     Public MustInherit Class WorkflowTemplateStorageWithDescriptionBase
    	Inherits WorkflowTemplateStorageBase
C++ __Копировать
     public ref class WorkflowTemplateStorageWithDescriptionBase abstract : public WorkflowTemplateStorageBase
F# __Копировать
     [<AbstractClassAttribute>]
    type WorkflowTemplateStorageWithDescriptionBase = 
        class
            inherit WorkflowTemplateStorageBase
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[StorageObject](T_Tessa_Platform_Storage_StorageObject.htm) __[WorkflowStorageBase](T_Tessa_Workflow_Storage_WorkflowStorageBase.htm) __[WorkflowTemplateStorageBase](T_Tessa_Workflow_Storage_WorkflowTemplateStorageBase.htm) __ WorkflowTemplateStorageWithDescriptionBase
Derived
[Tessa.Workflow.Storage.WorkflowNodeStorage](T_Tessa_Workflow_Storage_WorkflowNodeStorage.htm)
[Tessa.Workflow.Storage.WorkflowProcessStorage](T_Tessa_Workflow_Storage_WorkflowProcessStorage.htm)
##  __Конструкторы
[WorkflowTemplateStorageWithDescriptionBase(Dictionary<String, Object>,
WorkflowTemplateStorageBase)](M_Tessa_Workflow_Storage_WorkflowTemplateStorageWithDescriptionBase__ctor.htm)|
Инициализирует новый экземпляр класса
WorkflowTemplateStorageWithDescriptionBase  
---|---  
[WorkflowTemplateStorageWithDescriptionBase(SerializationInfo,
StreamingContext)](M_Tessa_Workflow_Storage_WorkflowTemplateStorageWithDescriptionBase__ctor_1.htm)|
Инициализирует новый экземпляр класса
WorkflowTemplateStorageWithDescriptionBase  
##  __Свойства
[Caption](P_Tessa_Workflow_Storage_WorkflowTemplateStorageBase_Caption.htm)|
Отображаемый заголовок объекта.  
(Унаследован от
[WorkflowTemplateStorageBase](T_Tessa_Workflow_Storage_WorkflowTemplateStorageBase.htm))  
---|---  
[Description](P_Tessa_Workflow_Storage_WorkflowTemplateStorageWithDescriptionBase_Description.htm)|
Описание объекта  
[DynamicHash](P_Tessa_Workflow_Storage_WorkflowStorageBase_DynamicHash.htm)|
Хеш объекта в dynamic  
(Унаследован от
[WorkflowStorageBase](T_Tessa_Workflow_Storage_WorkflowStorageBase.htm))  
[Hash](P_Tessa_Workflow_Storage_WorkflowStorageBase_Hash.htm)|  Параметры
объекта  
(Унаследован от
[WorkflowStorageBase](T_Tessa_Workflow_Storage_WorkflowStorageBase.htm))  
[ID](P_Tessa_Workflow_Storage_WorkflowStorageBase_ID.htm)|  ID объекта  
(Унаследован от
[WorkflowStorageBase](T_Tessa_Workflow_Storage_WorkflowStorageBase.htm))  
[Name](P_Tessa_Workflow_Storage_WorkflowTemplateStorageBase_Name.htm)|  Имя
объекта.  
(Унаследован от
[WorkflowTemplateStorageBase](T_Tessa_Workflow_Storage_WorkflowTemplateStorageBase.htm))  
[ParentObject](P_Tessa_Workflow_Storage_WorkflowTemplateStorageBase_ParentObject.htm)|
Родительский объект.  
(Унаследован от
[WorkflowTemplateStorageBase](T_Tessa_Workflow_Storage_WorkflowTemplateStorageBase.htm))  
##  __Методы
[CallIsChangedChanged](M_Tessa_Workflow_Storage_WorkflowStorageBase_CallIsChangedChanged.htm)|  
(Унаследован от
[WorkflowStorageBase](T_Tessa_Workflow_Storage_WorkflowStorageBase.htm))  
---|---  
[CheckName](M_Tessa_Workflow_Storage_WorkflowTemplateStorageBase_CheckName.htm)|
Метод проверяет, допустимо ли новое указанное имя для изменяемого объекта.  
(Унаследован от
[WorkflowTemplateStorageBase](T_Tessa_Workflow_Storage_WorkflowTemplateStorageBase.htm))  
[CleanCollectionAndSetNullIfEmpty](M_Tessa_Platform_Storage_StorageObject_CleanCollectionAndSetNullIfEmpty.htm)|
Очищает коллекцию, найденную по ключу key, после чего устанавливает null на
место коллекции, если она стала пустой.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[ClearCache](M_Tessa_Platform_Storage_StorageObject_ClearCache.htm)|  Очищает
внутренний кэш декораторов.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[ClearChanges](M_Tessa_Workflow_Storage_WorkflowStorageBase_ClearChanges.htm)|
Метод для очистки информации об изменении объекта  
(Унаследован от
[WorkflowStorageBase](T_Tessa_Workflow_Storage_WorkflowStorageBase.htm))  
[Clone](M_Tessa_Workflow_Storage_WorkflowStorageBase_Clone.htm)|  Метод для
создания клона объекта  
(Унаследован от
[WorkflowStorageBase](T_Tessa_Workflow_Storage_WorkflowStorageBase.htm))  
[CloneStorage](M_Tessa_Workflow_Storage_WorkflowStorageBase_CloneStorage.htm)|  
(Унаследован от
[WorkflowStorageBase](T_Tessa_Workflow_Storage_WorkflowStorageBase.htm))  
[ContainsKey](M_Tessa_Platform_Storage_StorageObject_ContainsKey.htm)|
Возвращает признак того, что элемент с заданным ключом содержится в хранилище.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[CorrectName](M_Tessa_Workflow_Storage_WorkflowTemplateStorageBase_CorrectName.htm)|
Метод для установки имени с исправлением, если такое имя уже есть.  
(Унаследован от
[WorkflowTemplateStorageBase](T_Tessa_Workflow_Storage_WorkflowTemplateStorageBase.htm))  
[EnsureCacheResolved](M_Tessa_Platform_Storage_StorageObject_EnsureCacheResolved.htm)|
Инициализирует объект-обёртку для всех значений, в т.ч. для вложенных
объектов. Рекомендуется выполнять при создании заполненного объекта перед
асинхронным обращением к его вложенным объектам.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
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
[FromJsonCore](M_Tessa_Platform_Storage_StorageObject_FromJsonCore.htm)|
Устанавливает содержимое объекта в соответствии с данными, десериализованными
из текстового JSON. Возвращает текущий объект для цепочки вызовов. Рассмотрите
использование метода
[ToTypedJson(Boolean)](M_Tessa_Platform_Storage_StorageObject_ToTypedJson.htm)
для сериализации с сохранением полной информации по типам, которую можно будет
восстановить в методе FromTypedJson.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[FromTypedJsonCore](M_Tessa_Platform_Storage_StorageObject_FromTypedJsonCore.htm)|
Устанавливает содержимое объекта в соответствии с данными, десериализованными
из текстового JSON с сохранением типов. Используйте метод
[ToTypedJson(Boolean)](M_Tessa_Platform_Storage_StorageObject_ToTypedJson.htm)
для сериализации с сохранением типов. Для десериализации других объектов, у
которых нет метода FromTypedJson (например, request/response), используйте
метод
[DeserializeFromTypedJson(String)](M_Tessa_Platform_Storage_StorageHelper_DeserializeFromTypedJson.htm),
записав полученную структуру в объект obj.SetStorage(storage).  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[Get<T>(String)](M_Tessa_Platform_Storage_StorageObject_Get__1.htm)|
Возвращает строго типизированное значение объекта из хранилища по заданному
ключу.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[Get<T>(String,
Func<Object>)](M_Tessa_Platform_Storage_StorageObject_Get__1_1.htm)|
Возвращает строго типизированное значение объекта из хранилища по заданнному
ключу с указанием фабрики defaultValueFunc, создающей значение по умолчанию и
добавляющей его в хранилище, если оно было равно null.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[GetDictionary<T>](M_Tessa_Platform_Storage_StorageObject_GetDictionary__1.htm)|
Возвращает декоратор для коллекции пар ключ / значение, полученный из
хранилища по заданному ключу или созданный посредством заданной фабрики
defaultDictionaryFunc, и добавленный в хранилище, если он там отсутствует.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetList<T>](M_Tessa_Platform_Storage_StorageObject_GetList__1.htm)|
Возвращает декоратор для коллекции объектов, полученный из хранилища по
заданному ключу или созданный посредством заданной фабрики defaultListFunc, и
добавленный в хранилище, если он там отсутствует.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[GetObjectData](M_Tessa_Platform_Storage_StorageObject_GetObjectData.htm)|
Записывает сериализованные данные текущего объекта в указанный объект
[System.Runtime.Serialization.SerializationInfo].  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[GetObjectName](M_Tessa_Workflow_Storage_WorkflowTemplateStorageBase_GetObjectName.htm)|
Метод для получения имени объекта с его заголовком.  
(Унаследован от
[WorkflowTemplateStorageBase](T_Tessa_Workflow_Storage_WorkflowTemplateStorageBase.htm))  
[GetStorage](M_Tessa_Platform_Storage_StorageObject_GetStorage.htm)|
Возвращает хранилище Dictionary<string, object>, декоратором для которого
является текущий объект.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[HasChanges](M_Tessa_Workflow_Storage_WorkflowStorageBase_HasChanges.htm)|
Метод для проверки наличия изменений у объекта  
(Унаследован от
[WorkflowStorageBase](T_Tessa_Workflow_Storage_WorkflowStorageBase.htm))  
[Init](M_Tessa_Platform_Storage_StorageObject_Init.htm)|  Инициализирует
значение объекта с заданным ключом, если он отсутствовал в хранилище.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[InitNotNull](M_Tessa_Platform_Storage_StorageObject_InitNotNull.htm)|
Инициализирует значение объекта с заданным ключом, если он отсутствовал в
хранилище или был равен null, посредством фабрики объектов.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[MarkChanged](M_Tessa_Workflow_Storage_WorkflowStorageBase_MarkChanged.htm)|  
(Унаследован от
[WorkflowStorageBase](T_Tessa_Workflow_Storage_WorkflowStorageBase.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[OnPropertyChanged(PropertyChangedEventArgs)](M_Tessa_Workflow_Storage_WorkflowStorageBase_OnPropertyChanged.htm)|
Уведомляет об изменении свойства с именем, заданным в аргументах события.  
(Унаследован от
[WorkflowStorageBase](T_Tessa_Workflow_Storage_WorkflowStorageBase.htm))  
[OnPropertyChanged(String)](M_Tessa_Workflow_Storage_WorkflowStorageBase_OnPropertyChanged_1.htm)|
Уведомляет об изменении свойства с заданным именем у объекта.  
(Унаследован от
[WorkflowStorageBase](T_Tessa_Workflow_Storage_WorkflowStorageBase.htm))  
[OnPropertyChangedInternal](M_Tessa_Workflow_Storage_WorkflowStorageBase_OnPropertyChangedInternal.htm)|  
(Унаследован от
[WorkflowStorageBase](T_Tessa_Workflow_Storage_WorkflowStorageBase.htm))  
[Remove](M_Tessa_Platform_Storage_StorageObject_Remove.htm)|  Удаляет объект с
заданным ключом из хранилища.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[RemoveData](M_Tessa_Workflow_Storage_WorkflowTemplateStorageBase_RemoveData.htm)|
Метод для удаления данных из шаблона.  
(Унаследован от
[WorkflowTemplateStorageBase](T_Tessa_Workflow_Storage_WorkflowTemplateStorageBase.htm))  
[Set<T>](M_Tessa_Platform_Storage_StorageObject_Set__1.htm)|  Устанавливает
значение в хранилище по заданному ключу. При этом не изменяется внутренний кэш
декораторов, поэтому метод следует использовать только для примитивных типов.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[SetName](M_Tessa_Workflow_Storage_WorkflowTemplateStorageBase_SetName.htm)|
Устанавливает имя объекта и проверяет его существование среди других объектов.  
(Унаследован от
[WorkflowTemplateStorageBase](T_Tessa_Workflow_Storage_WorkflowTemplateStorageBase.htm))  
[SetNull](M_Tessa_Platform_Storage_StorageObject_SetNull.htm)|  Устанавливает
значение null для элемента по заданному ключу и удаляет предыдущий элемент из
внутреннего кэша декораторов.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[SetNullIfEmptyEnumerable](M_Tessa_Platform_Storage_StorageObject_SetNullIfEmptyEnumerable.htm)|
Устанавливает равным null элемент с ключом key, если он является пустым
перечислением
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable).  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[SetStorage(Dictionary<String,
Object>)](M_Tessa_Platform_Storage_StorageObject_SetStorage.htm)|
Устанавливает хранилище Dictionary<string, object>, декоратором для которого
является текущий объект, посредством копирования значений из заданного
хранилища. Если текущий объект реализует
[IStorageNotificationReceiver](T_Tessa_Platform_Storage_IStorageNotificationReceiver.htm),
то для него вызывается метод
[NotifyStorageUpdated()](M_Tessa_Platform_Storage_IStorageNotificationReceiver_NotifyStorageUpdated.htm).  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[SetStorage(IStorageObjectProvider)](M_Tessa_Platform_Storage_StorageObject_SetStorage_1.htm)|
Устанавливает хранилище Dictionary<string, object>, декоратором для которого
является текущий объект, посредством копирования значений из хранилища
заданного объекта. Если текущий объект реализует
[IStorageNotificationReceiver](T_Tessa_Platform_Storage_IStorageNotificationReceiver.htm),
то для него вызывается метод
[NotifyStorageUpdated()](M_Tessa_Platform_Storage_IStorageNotificationReceiver_NotifyStorageUpdated.htm).  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[SetStorageValue](M_Tessa_Platform_Storage_StorageObject_SetStorageValue.htm)|
Устанавливает значение объекта, реализующего
[IStorageProvider](T_Tessa_Platform_Storage_IStorageProvider.htm), в хранилище
по заданному ключу. При этом также изменяется внутренний кэш декораторов,
поэтому метод следует использовать для декораторов.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[ToDynamic](M_Tessa_Platform_Storage_StorageObject_ToDynamic.htm)|  Возвращает
объект, осуществляющий доступ к хранилищу, декоратором для которого является
текущий объект, через позднее связывание.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[ToJson](M_Tessa_Platform_Storage_StorageObject_ToJson.htm)|  Сериализует
объект в текстовый JSON. Рассмотрите использование метода
[ToTypedJson(Boolean)](M_Tessa_Platform_Storage_StorageObject_ToTypedJson.htm)
для сериализации с сохранением полной информации по типам, которую можно будет
восстановить в методе FromTypedJson.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToTypedJson](M_Tessa_Platform_Storage_StorageObject_ToTypedJson.htm)|
Сериализует объект в текстовый JSON с сохранением информации по типам для всех
подобъектов, в т.ч. для Info. Используйте метод FromTypedJson для
десериализации. Для сериализации других объектов, у которых нет метода
ToTypedJson (например, request/response), используйте метод
[!:StorageHelper.SerializeToTypedJson(Dictionary<string,object>,bool)],
передав в него структуру объекта obj.GetStorage().  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[TryGet<T>](M_Tessa_Platform_Storage_StorageObject_TryGet__1.htm)|  Возвращает
строго типизированное значение объекта из хранилища по заданному ключу или
default(T), если объект по заданному ключу не найден.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[TryGetDictionary<T>](M_Tessa_Platform_Storage_StorageObject_TryGetDictionary__1.htm)|
Возвращает строго типизированное значение объекта Dictionary<string, object>
из хранилища по заданному ключу или default(T), если объект по заданному ключу
не найден.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[TryGetList<T>](M_Tessa_Platform_Storage_StorageObject_TryGetList__1.htm)|
Возвращает строго типизированное значение объекта List<object> из хранилища по
заданному ключу или default(T), если объект по заданному ключу не найден.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[TryGetString](M_Tessa_Platform_Storage_StorageObject_TryGetString.htm)|
Возвращает строковое представление для значения объекта из хранилища по
заданному ключу или null, если объект по заданному ключу не найден.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[UpdateData](M_Tessa_Workflow_Storage_WorkflowTemplateStorageWithDescriptionBase_UpdateData.htm)|  
(Переопределяет
[WorkflowTemplateStorageBase.UpdateData(WorkflowStorageBase)](M_Tessa_Workflow_Storage_WorkflowTemplateStorageBase_UpdateData.htm))  
##  __События
[PropertyChanged](E_Tessa_Workflow_Storage_WorkflowStorageBase_PropertyChanged.htm)|
Событие, уведомляющее об изменении свойства с определённым именем у модели
представления.  
(Унаследован от
[WorkflowStorageBase](T_Tessa_Workflow_Storage_WorkflowStorageBase.htm))  
---|---  
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
[Tessa.Workflow.Storage - пространство имён](N_Tessa_Workflow_Storage.htm)
