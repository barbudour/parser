# NumberQueue(IStorageObjectProvider) - конструктор
Создаёт экземпляр класса с указанием объекта, предоставляющего доступ к
хранилищу, декоратором для которого является создаваемый объект.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public NumberQueue(
    	IStorageObjectProvider storageProvider
    )
VB __Копировать
     Public Sub New ( 
    	storageProvider As IStorageObjectProvider
    )
C++ __Копировать
     public:
    NumberQueue(
    	IStorageObjectProvider^ storageProvider
    )
F# __Копировать
     new : 
            storageProvider : IStorageObjectProvider -> NumberQueue
#### Параметры
storageProvider
[IStorageObjectProvider](T_Tessa_Platform_Storage_IStorageObjectProvider.htm)
     Объект, предоставляющий доступ к хранилищу Dictionary<string, object>, декоратором для которого является создаваемый объект. 
## __См. также
#### Ссылки
[NumberQueue - ](T_Tessa_Cards_Numbers_NumberQueue.htm)
[NumberQueue - перегрузка](Overload_Tessa_Cards_Numbers_NumberQueue__ctor.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
