# ApplicationPackageFile.FromStorage - метод
Создаёт новый объект
[ApplicationPackageFile](T_Tessa_Applications_Package_ApplicationPackageFile.htm)
и инициализирует его данными из указанного элемента хранилища.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Package](N_Tessa_Applications_Package.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static ApplicationPackageFile FromStorage(
    	IStorageElement storageElement
    )
VB __Копировать
     Public Shared Function FromStorage ( 
    	storageElement As IStorageElement
    ) As ApplicationPackageFile
C++ __Копировать
     public:
    static ApplicationPackageFile^ FromStorage(
    	IStorageElement^ storageElement
    )
F# __Копировать
     static member FromStorage : 
            storageElement : IStorageElement -> ApplicationPackageFile 
#### Параметры
storageElement
[IStorageElement](T_Tessa_Applications_Containers_Storage_IStorageElement.htm)
    Элемент хранилища.
#### Возвращаемое значение
[ApplicationPackageFile](T_Tessa_Applications_Package_ApplicationPackageFile.htm)  
Новый объект
[ApplicationPackageFile](T_Tessa_Applications_Package_ApplicationPackageFile.htm).
##  __См. также
#### Ссылки
[ApplicationPackageFile -
](T_Tessa_Applications_Package_ApplicationPackageFile.htm)
[Tessa.Applications.Package - пространство
имён](N_Tessa_Applications_Package.htm)
